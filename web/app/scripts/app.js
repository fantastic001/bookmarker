'use strict';

require('angular');

/**
 *
 */
angular.module('Bookmarker', [
    require('angular-ui-router'),
    require('angular-sanitize')
  ])

  .config(require('./config.js'))

  .controller('AppController', require('./app-controller.js'))

  .constant('API_URL', 'http://0.0.0.0:8000/')

  .constant("BACKEND_URL", "http://0.0.0.0:8000/");


