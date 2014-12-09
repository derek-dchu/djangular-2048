'use strict';

angular.module('Grid')
.directive('grid', function() {
        return {
            restrict: 'A',
            require: 'ngModel',
            scope: {
                ngModel: '='
            },
            templateUrl: 'static/angular-2048/app/scripts/grid/grid.html'
        }
    });