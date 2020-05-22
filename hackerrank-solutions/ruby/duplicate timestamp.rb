require 'set'

def parse_date_from_log(l_data)
  str_date = l_data.split(' - - [')[1].split('] ').first.split(' -').first
end

input_file_path = File.join(File.dirname(__FILE__), 'input.txt')
output_file_path = File.join(File.dirname(__FILE__), 'req_input.txt')
duplicate_timestamps = Set.new()
last_timestamp = ''

File.foreach(input_file_path) do |log| 
  timestamp = parse_date_from_log(log)
  if last_timestamp == timestamp
    duplicate_timestamps.add(timestamp)
  else
    last_timestamp = timestamp
  end
end
  
File.open(output_file_path, "w+") do |f|
  f.puts(duplicate_timestamps.to_a)
end