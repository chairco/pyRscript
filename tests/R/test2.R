# load necessary package
library(logging)

# setting logging
logReset()
basicConfig(level='FINEST')

args <- commandArgs(TRUE)
sys.toolid <- args[2]

if (length(args) <= 1) {
    loginfo('Arguments toolid and mode need supplid.')
} else if (args[1] == 'test' & args[2] != 'test2') {
    loginfo(sprintf('Input 2 args "test" and "not test2": %s %s', args[1], args[2]))
} else {
    loginfo(sprintf('Input 2 args:, args: %s %s', args[1], args[2]))
}
