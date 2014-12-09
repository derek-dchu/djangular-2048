'use strict';

angular.module('Grid')
.directive('tile', function() {
        return {
            restrict: 'A',
            require: 'ngModel',
            scope: {
                ngModel: '='
            },
            templateUrl: 'static/angular-2048/app/scripts/grid/tile.html'
        }
    });