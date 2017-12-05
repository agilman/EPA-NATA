var mapper = angular.module("mapper",['leaflet-directive','ui.bootstrap']);

mapper.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
