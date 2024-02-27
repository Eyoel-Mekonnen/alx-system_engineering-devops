#!/usr/bin/env ruby
#matches anything anything between hbt and n
puts ARGV[0].scan(/hb(t+)n/).join
