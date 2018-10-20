#!/usr/bin/env ruby
require 'date'

#TODO: Add values for your country!
LIFE_EXPECTANCY = { 
			all: {
				world: 70.5,
			},
			female:{
				world: 72.75, 
			},
			male: {
				world: 68.25,
			}
}

CHAR_WEEK_SPENT = "\u25A3"
CHAR_WEEK_LEFT  = "\u2610"

def print_calendar(total_weeks, weeks_spent, symbol_spent, symbol_left)
	print_x_axis
	(total_weeks + 1).times do |week|
		printf " " + ((week < weeks_spent) ? symbol_spent : symbol_left).to_s unless week == 0
		printf "\n#{(week/52).to_i.to_s.rjust(2,"0")}" if (week % 52 == 0)
	end 
end

def print_x_axis
	printf "  "
	step = 5
	52.times { |t| printf  (((t+1)%step == 0)? (t+1).to_s.rjust(2, " "): "  ")}
end

def print_help_and_exit
	puts \
"""USAGE #{$0} [OPTIONS] 
Print a representation of your life in weeks (weeks passed: #{CHAR_WEEK_SPENT}, weeks left #{CHAR_WEEK_LEFT})

Options: 
	-m 		Use life expectancy for males
	-f 		Use life expectancy for females
	-b YYYY-mm-dd	Specify day of birth
	-h 		Print this message and exit\n
"""
	exit
end


 
locale = :world
life_expectancy = nil
birthday = nil 

while arg = ARGV.shift
	case arg
		when "-h"
			print_help_and_exit
		when "-m"
			print_help_and_exit if life_expectancy
			life_expectancy = LIFE_EXPECTANCY[:male][locale]
		when "-f"
			print_help_and_exit if life_expectancy
			life_expectancy = LIFE_EXPECTANCY[:female][locale]
		when "-b"
			birthday_str = ARGV.shift
			print_help_and_exit unless birthday_str
			birthday = Date.parse(birthday_str).to_time rescue print_help_and_exit
		else
			print_help_and_exit
	end
end


life_expectancy ||= LIFE_EXPECTANCY[:all][locale]

birthday ||= Time.new(2000,12,31) 

WEEKS_PER_YEAR = 52.1775 
DAYS_PER_YEAR  = 365.25 

time_of_death = birthday + life_expectancy * DAYS_PER_YEAR * 24 * 60 *60
total_weeks = (life_expectancy * WEEKS_PER_YEAR).to_i
days_left  =  (time_of_death.to_i - Time.now.to_i) / 60 /60 / 24 
weeks_left = days_left / 7
years_left = (days_left / DAYS_PER_YEAR).to_i
weeks_spent = total_weeks - weeks_left

print_calendar(total_weeks, weeks_spent, CHAR_WEEK_SPENT, CHAR_WEEK_LEFT ) 
printf " 💀\n"
puts "\nTIME LEFT: #{days_left} days / #{weeks_left} weeks/ #{years_left} years"
percent_spent = (100.0*weeks_spent/total_weeks.to_f)
percent_left = 100 - percent_spent.to_i
puts "SPENT LIFETIME: #{percent_spent.round(4).to_s}%"
puts ("▇"*percent_spent.to_i + "░"*percent_left)

