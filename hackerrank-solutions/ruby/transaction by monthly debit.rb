#!/bin/ruby

require 'json'
require 'stringio'


require 'net/http'
require 'time'

#
# Complete the 'getUserTransaction' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER uid
#  2. STRING txnType
#  3. STRING monthYear
#
#  https://jsonmock.hackerrank.com/api/transactions/search?txnType=

BASE_URL = "https://jsonmock.hackerrank.com/api/transactions/search"
def getUserTransaction(uid, txnType, monthYear)
    puts "req data uid: #{uid}, txnType: #{txnType}, monthYear: #{monthYear}"
    options = {
        date: month_year_to_date(monthYear),
        page: 1,
        req_params: {
            userId: uid
        },
        prev_data: []
    }

    if txnType == 'debit'
        options[:req_params][:txnType] = txnType
    end

    # fetch all the transactions
    transactions = getAllTransaction(BASE_URL, options)
    
    debit_counter = 0
    total_debit = 0
    target_transactions = []
    transactions.each do |t|
        if t['txnType'] == 'debit'
            debit_counter += 1
            total_debit += to_num(t['amount'])
        end

        if t['txnType'] == txnType
            target_transactions << t
        end
    end
    avg_debit = total_debit / debit_counter
    
    # take filtered transaction ids
    transaction_ids = []
    target_transactions.each do |t|
      transaction_ids << t['id'] if to_num(t['amount']) > avg_debit
    end

    # no transaction found
    if transaction_ids.size.zero?
      return [-1]
    end

    transaction_ids
end

def getAllTransaction(url, options = {})
    page = options[:page]
    date = options[:date]
    req_params = options[:req_params]
    uri = URI(url)
    uri.query = URI.encode_www_form(req_params.merge({page: page}))
    begin
      res = JSON.parse(Net::HTTP.get_response(uri).body)
      
      # filter by expected time
      current_data = res['data'].select do |data|
        res_date = epoch_to_date(data['timestamp']).to_datetime
        data['timestamp'] = res_date
        res_date.year == date.year && res_date.month == date.month
      end
      
      if has_next_page?(res)
          options[:prev_data] = options[:prev_data] + current_data
          options[:page] = options[:page] + 1
          return getAllTransaction(url, options)
      end

      options[:prev_data] + current_data
    rescue Exception => e
        put "There was something wrong #{e.to_s}"
    end
end


# epoch time to date
def epoch_to_date(epoch_time)
    Time.at(0, epoch_time , :millisecond).to_datetime
end

# convert m-y to date object
def month_year_to_date(month_year)
    Time.parse("01-#{month_year}")
end

def has_next_page?(res)
    res['total_pages'] > res['page'].to_i
end

def to_num(str_amount)
    str_amount[1..-1].gsub(',', '').to_f
end
fptr = File.open(ENV['OUTPUT_PATH'], 'w')