# load necessary package
library(logging)

# setting logging
logReset()
basicConfig(level='FINEST')

args <- commandArgs(TRUE)
sys.toolid <- args[2]

if (length(args) <= 1) {
    loginfo('Arguments toolid and mode need supplid.')
} else if (args[1] == 'ETL' & args[2] != 'NIKON') {
    loginfo(sprintf('ETL, args: %s %s', args[1], args[2]))
} else {
    loginfo(sprintf('ETL & NIKON, args: %s %s', args[1], args[2]))
}
