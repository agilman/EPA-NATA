mapper.controller("tractsController",['$scope','$log','$http',function($scope,$log,$http){
    $log.log("Hello from tracts controller");

    //$scope.selectedCounty = null;
    $scope.rawTractsData=null;
    
    
    $scope.changeState = function(data){
	loadCounties(data);
    };

    function loadCounties(stateId){
	$http.get('/api/stateCounties/'+stateId).then(function(data){
	    $scope.counties = data.data;
	});
	
    }

    $scope.changeCounty = function(countyId){
	$log.log("CHanged county...load up tracts",$scope.selectedState,countyId);
	$http.get('/api/diesel/'+$scope.selectedState+'/'+countyId).then(function(data){
	    $log.log(data.data);
	    $scope.rawTractsData = data.data;
	});
    }
}]);
