require 'set'

# read the string filename
filename = gets.strip
input_file_path = File.join(File.dirname(__FILE__), filename)
output_file_path = File.join(File.dirname(__FILE__), "req_#{filename}")
duplicate_timestamps = Set.new()
last_timestamp = ''

File.foreach(input_file_path) do |log|
  # parse timestamp from log
  timestamp = log.split(' - - [')[1].split('] ').first.split(' -').first

  if last_timestamp == timestamp
    duplicate_timestamps.add(timestamp)
  else
    last_timestamp = timestamp
  end
end

# write duplicate timestamp to file
File.open(output_file_path, "w+") do |f|
  f.puts(duplicate_timestamps.to_a)
end