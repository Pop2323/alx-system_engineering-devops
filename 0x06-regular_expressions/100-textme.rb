#!/usr/bin/env ruby
# For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon,
# a TextMe VoIP Engineer comes to you and explains she wants
# to run some statistics on the TextMe app text messages transactions.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
