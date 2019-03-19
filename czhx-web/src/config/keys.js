/**
 * keys.js - decide which set of keys to export
 */
if (process.env.NODE_ENV === 'production') {
    module.exports = require('./prod');
} else {
    module.exports = require('./dev');
}