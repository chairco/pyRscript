oldw <- getOption("warn")
options(warn = -1)

# load necessary package
library(optparse)
library(logging)

# setting logging
logReset()
basicConfig(level='FINEST')

# commmand line args and test if there is at least one argument: if not, return an error
option_list = list(
  make_option(c("-d", "--id"), type="character", default=NULL, 
              help="id, ex: sn1234", metavar="character"),
  make_option(c("-t", "--time"), type="character", default=NULL, 
              help="time, ex: 2017-07-13 20:00:27", metavar="character")
);

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);


if (is.null(opt$id) || is.null(opt$time)){
    print_help(opt_parser)
    stop("At least one argument must be supplied (input ID and Time).\n", call.=FALSE)
} else{
    loginfo('Execute R')
    loginfo(sprintf('id: %s, time: %s', opt$id, opt$time))
}