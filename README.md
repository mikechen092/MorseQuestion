# MorseQuestion

## Intro
When creating the classes to solve the pricing statistics problem, I created two classes
and a separate wrapper script that would have the command line interface and would run
obtain the information from the classes. The two classes I created are the Day_Info class
and the Database class. The Day_Info class was a way to store all the information (datetime,
price,units) all within a single object. The Database class was a way to store the different 
Day_Info objects so that the wrapper class could access the information. The wrapper script 
consisted of four functions. The functions are the main function, the parse_file function, 
the get_statistics function, and the search_db function. The main function takes care of 
the command line interface and calls the parse_file function on the file path provided from
the CLI. The parse_file parses the file and creates Day_Info objects and places them in a 
Database object provided. The main function also calls either the search_db function or the 
get_statistics function depending on how many datetime objects are provided to the CLI. The 
search_db function searches the Database object provided and prints the price of the datetime 
provided, the average of the adjacent prices in terms of datetime, or the nearest price if 
the other two options are not viable. The get_statistics function takes two datetimes provided 
by the CLI, and finds every entry in the range between the two datetimes. It then prints out
the desired statistics.

to run from command line run: python statistics_tool.py [filepath] [D [d]]

give a single datetime object to run a search to return a price, give two to get statistics
about the defined range


## Day_Info.py

The Day_Info class was created to store all the information given in the file a single place
for each entry. Constructor takes a datetime, price, and a number of units. The constructor
assumes that the information being passed is valid and does not check to make sure each field
is of the correct type. The methods written are methods to obtain the information stored in each
field as well as a comparision method. The compare method, given another Day_Info object, will
return true or false depending on if the given Day_Info object contains the same information 
the current Day_Info object contains. 

## Database.py

The Database class was created to store the Day_Info class in a relevant way. The Day_Info
objects are stored in ascending order from smallest datetime to largest datetime. The methods
include add_entry, is_empty, get_min, get_max, lookup, and lookup_range. I though about using
a dictionary instead of an array where the date would hash to the Day_Info object, but I did
not have time to finish implementing it.

### add_entry

The add_entry is the way to add Day_Info objects to the database. It does not check that the
object being passed is Day_Info object. The method searches for the first entry in the db array
that has a larger datetime value that the datetime in the Day_Info object wanting to be added. 
The worst case runtime for this method is going to be O(N) where N is the number of entries in 
the db array right now. If a dictionary were used, inserting the new Day_Info object would be
constant, but there would still need to be some auxiliary structure to store a sorted list of
keys to the dictionary, so it would be log2(N) because you would just use binary search to 
find the new location for the new key that maps to the new Day_Info object.

### is_empty

The is_empty is a way to make sure that the function calling on the database can know if the 
there are any entries in the database. It is constant time O(1) because len() in python is 
constant. It would not change runtime from list to dictionary

### get_min

The get_min is a fast way to get the smallest datetime in the list without having to query
for it. This is useful in situations where you want to check if the datetime being searched
for is within the range in the database. The runtime is constant O(1) time. It would not change
when going from list to dictionary.

### get_max

Similar to the get_min, but gets the largest datetime in the list. Also similar to the get_min,
get_max is useful in range checks of the datetimes of the database. Runtime is the same.

### lookup

The lookup method returns a tuple of two Day_Info objects. By stepping through the db array,
it finds either the first Day_info object whose datetime is greater than the given datetime
and returns the found Day_Info object along with the previous Day_Info object in the array,
or finds the corresponding Day_Info with the same date as the one given and returns the exact
Day_Info twice in a tuple. I decided to have the method return a tuple of Day_Info objects
because I wanted it to be consistent throughout the test cases. I could have printed the prices
and not had to worry about what to return, but I decided for that it would be better to leave
that functionality to the wrapper function rather than have that be a quality of the database
class. The runtime for this method is O(N) where N is the number of entries in the Database.
If I had fully optimized the solution, the runtime would be either O(1) if the datetime was
in the dictionary and log2(N) to search for the adjacent datetimes.  

### lookup_range

The lookup_range method returns an array of Day_Info objects that have datetimes that lie 
between the two datetimes provided. The lookup_range assumes the first datetime is smaller
than the second datetime. By finding the first Day_Info object with a date greater than or
equal to the first provided date, you can find the index of the lower bound of the range of
datetimes in the db array. By finding the first Day_Info object that is greater than the 
second provided date, you can find the index of the upper bound. If the two loops conclude
without setting the high/low index values, they default to the preset values of the length
of the db array and zero respectively. This means the whole array is in the provided datetime
range. The runtime of this method is O(2*N) or just O(N) because in the worse case, both loops
would run till the very last item. If I had fully optimized the solution, the runtime
would change to O(2*log2(N)) or just O(log2(N)). This is because given a sorted array you could
use binary search to find the indices you need.

## Statistics Tool

### parse_file

The parse_file function takes in a database, empty or not empty, and fills the database with
the Day_Info objects created from reading information from the file. The function checks that 
the file can be opened and also checks that the information in the file is in the correct format.
It also converts the datetime parsed from the file into UTC so there is no confusion about
timezones. The runtime is O(M^2) where M is the number of lines in the file assuming that the
dateutil.parser runs in constant time. This is because on every iteration of the loop the
Database method add_entry is called.  

### search_db

The search_db function takes in a database and a datetime to query the database. The first
thing the function checks is the length of the database input. If the database is empty, then
no information can be queried, so it prints out an error message and returns. If the datetime
object is not already in UTC, the function then converts the datetime into the appropriate 
timezone. If there is something else that is not a datetime object passed into the function,
then the function will print out an error message and return. The search_db main functionality 
lies in calling the Database method lookup. If the two Day_Info objects in the tuple are the
same then the datetime queried is in the database and the price is printed. If the two Day_Info
objects are different then the datetime queried is not in the database and the average of the
two prices are output. The runtime is O(N) where N is the number of entries in the database. 
This is because the function calls the Database method lookup which is O(N). 

### get_statistics

The get_statistics function takes in a database and two datetime objects defining the range
to lookup using the Database method lookup_range. The function does not assume the Database
object has entries within it. The function also does not assume that the first datetime is the
smaller datetime. If the range defined by the two datetimes do not encompass any entries in
the database, then the function calls search_db instead and prints out a message letting 
the user know. The function calculates min and max prices of the array that is returned by
lookup_range. It also calculates the average price, the standard deviation of the number of
units, and the median of all the units of the Day_Info objects returned. The runtime of this
function is worst case O(3*N) or O(N) where N is the number of entries in the Database object
because it calls the Database function lookup_range and has two other for-loops running over
the entire array returned by lookup_range in series. 

### main

The main function take care of the command-line interface. Using argparse, I was able to 
create an argument for first the filename and then the list of datetimes. I assumed that 
the datetime object would be able to be passed directly to the CLI. The function then 
creates a new database object and calls parse_file on the filename input from the CLI and
adds them to the newly created Database object. Then depending on how many datetimes are
input from the command line, it either calls search_db or get_statistics. If there are too
many datetimes input into the command-line, then it prints out an error message and exits.
The runtime of this function is O(N^2 + N) or just O(N^2). This is because it always calls
parse_file which is O(N^2), and both search_db and get_statistics are O(N)

