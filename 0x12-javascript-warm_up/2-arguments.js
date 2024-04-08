#!/usr/bin/node
if (Process.argv.length === 2) {
    console.log('No Argument');
} else if (Process.argv.length === 3) {
    console.log('Argument Found');
} else {
    console.log('Arguments Found');
}
