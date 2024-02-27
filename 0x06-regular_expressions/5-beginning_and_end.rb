#!/usr/bin/env ruby
#mathces anyt charcter in between h and n
puts ARGV[0].scan(/^[h].+n$/).join
