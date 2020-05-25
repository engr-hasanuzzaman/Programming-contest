def countMeetings(firstDay, lastDay)
  booked_date = {}
  schedules = firstDay.zip(lastDay).sort_by{|a| [a.last, a.last - a.first] }
  meeting_count = 0
  schedules.each do |start_day, end_day|
    while start_day <= end_day
      if booked_date[start_day]
        start_day += 1
        next
      end

      booked_date[start_day] = true
      meeting_count += 1
      break
    end
  end

  meeting_count  
end