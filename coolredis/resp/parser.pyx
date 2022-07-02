from libc.stdlib cimport (
    strtoll,
)

cdef:
    char* LINE_TERMINATOR = "\r\n"

    char STRING_PREFIX = "+"
    char ERROR_PREFIX = "-"
    char INTEGER_PREFIX = ":"
    char BULK_STRING_PREFIX = "$"
    char ARRAY_PREFIX = "*"

    # Parsers for individual types, assuming the prefix and NL char has already been removed.
    char* parse_string(char* line):
        return line
    
    char* parse_error(char* line):
        return parse_string(line)
    
    long long int parse_int(char* line):
        return strtoll(line, NULL, 0)
    
    enum DataType:
        STRING = 0
        ERROR = 1
        INT = 2
        BULK_STRING = 3
        ARRAY = 4

cpdef struct ErrorType

cdef parse_type(bytes redis_line):
    cdef char* line = <char*> redis_line
    cdef first_byte = line[0]

    # Remove the first byte as its used to denote type.  
    line += 1  

    if first_byte == STRING_PREFIX:
        return parse_string(line)
    elif first_byte == ERROR_PREFIX:
        return parse_error(line)
    elif first_byte == INTEGER_PREFIX:
        return parse_int(line)
