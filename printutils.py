import datetime

def print_line(args):
    if args.verbose == 1:        
        print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + '-' * 72 )

def print_message(msg,args):
    if args.verbose == 1:
        print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - ' + str(msg) )
        
def print_new_process(msg,args):
    if args.verbose == 1:        
        print_line(args)
        print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - ' + str(msg) )
        
def print_end(msg,args):
    if args.verbose == 1:
        print_line(args)
        print( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - ' + str(msg) )        
        print_line(args)
