#!/usr/bin/env ruby
#matches 10 digits only
puts ARGV[0].scan(/^\d{10}$/).join
