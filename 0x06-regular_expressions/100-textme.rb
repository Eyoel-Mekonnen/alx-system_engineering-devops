#!/usr/bin/env ruby
#extracts sender , reciever and flags
from = ARGV[0].scan(/(?<=from:)[A-Za-z0-9\-\+]+(?=\])/).join
to =  ARGV[0].scan(/(?<=to:)[A-Za-z0-9\-\+]+(?=\])/).join
flags = ARGV[0].scan(/(?<=flags:)[0-9\-\:]+(?=\])/).join
puts "#{from},#{to},#{flags}"
