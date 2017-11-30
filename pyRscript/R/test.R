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
  make_option(c("-t", "--tid"), type="character", default=NULL, 
              help="toolid, ex: tlcd0501", metavar="character"),
  make_option(c("-s", "--start"), type="character", default=NULL, 
              help="start time, ex: 2017-07-13 20:00:27", metavar="character"),
  make_option(c("-e", "--end"), type="character", default=NULL, 
              help="end time, ex: 2017-07-14 20:00:27", metavar="character")
);

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);


if (is.null(opt$tid) || is.null(opt$start) || is.null(opt$end)){
    print_help(opt_parser)
    stop("At least one argument must be supplied (input start and end time).\n", call.=FALSE)
} else{
    loginfo('execute ROT...')
    loginfo(sprintf('tid: %s, st: %s, et: %s', opt$tid, opt$start, opt$end))
}