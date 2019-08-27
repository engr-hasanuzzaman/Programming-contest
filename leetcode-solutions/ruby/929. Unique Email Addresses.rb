# https://leetcode.com/problems/unique-email-addresses/
# @param {String[]} emails
# @return {Integer}
def num_unique_emails(emails)
  emails.map do |email|
      extract_email(email)
  end.uniq.count
end

def extract_email(s)
  name,domain = s.split('@')
  result_email = ''
  
  name.each_char do |c|
      return "#{result_email}@#{domain}" if c == '+'
      next if c == '.'
      result_email += c
  end
  
  "#{result_email}@#{domain}"
end