var app = angular.module('restapi.app', []);

app.controller('AppController', function($scope, $http) {
    $http.get('http://192.168.35.11:8080/api/places/').
    then(function(response) {
        $scope.places = response.data;
    });
});
