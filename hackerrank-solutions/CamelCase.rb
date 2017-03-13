#!/bin/ruby

s = gets.strip
print s.split(/(?=[A-Z])/).count
