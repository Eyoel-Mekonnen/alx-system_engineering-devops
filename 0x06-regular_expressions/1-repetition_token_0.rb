#!/usr/bin/env ruby
#matches anything anything between hbt and n
puts ARGV[0].scan(/hbt{2, 5}n/).join
