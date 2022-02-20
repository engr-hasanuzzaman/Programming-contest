=begin
Coding question - OCR recognises Strings written and unable to recognise some characters properly. 
After some processing you get Strings like S1 -> "A3BCD" which is equivalent to A***BCD (3 unknown characters which can be anything).
Given two such strings, identify if they can be equal. For example A3BCD is equal to A6 or A3BC1 etc.,. (I provided solution by exploding the string.
Replacing the numbers with those many blank characters, interviewer said this definitely works but not optimal - I'm assuming he expected a two pointer approach where each pointer points to each String and iterate)
=end

require 'rspec/autorun'

  def match_str(str1, str2)
    first = second = 0
    
    while first < str1.size && second < str2.size
      chr1 = str1[first]
      chr2 = str2[second]
      puts "----f #{first}, s #{second}, #{chr1} #{chr2}"
      if chr1 == chr2
        first += 1
        second += 1
      elsif is_char?(chr2) && is_char?(chr1)
        # puts "----return false #{chr2} #{chr1}"
        return false
      elsif is_digit?(str1[first]) && is_digit?(str2[second])
        d1 = str1[first].to_i
        d2 = str2[second].to_i
        if d1 == d2
          first += 1
          second += 1
        elsif d1 > d2
          second += 1
          str1[first] = (d1 - d2).to_s
        else
          first += 1
          str2[second] = (d2 - d1).to_s
        end
      else
        if is_digit?(chr1)
          d1 = str1[first].to_i
          if d1 == 1
            first += 1
          else
            str1[first] = (d1 - 1).to_s
          end
          second += 1
        else
          d2 = str2[second].to_i
          if d2 == 1
            second += 1
          else
            str2[second] = (d2 - 1).to_s
          end
          first += 1
        end
      end
    end
    puts "---#{first}, #{second}"
    first == str1.size && second == str2.size
  end
    
  def is_digit?(chr)
    chr.ord >= '0'.ord && chr.ord <= '9'.ord
  end
    
  def is_char?(chr)
    !is_digit?(chr)
  end

  RSpec.describe "#match_str" do
    it 'barks when spoken to' do
      expect(match_str('A6', 'A3BC1')).to eq(true)
      expect(match_str('ABC1', 'ABCD1')).to eq(false)
      expect(match_str('A3C1', 'ABCD1Q')).to eq(true)
      
    end
  end