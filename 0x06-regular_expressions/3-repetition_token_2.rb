#!/usr/bin/env ruby
#matches hbtn with min 1 and max 4
puts ARGV[0].scan(/hb{1,}tn/).join
