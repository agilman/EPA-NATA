mapper.controller("mainController",['$scope','$log','$http',function($scope,$log,$http){
    $scope.states = [];

    //get list of states
    function loadStates(){
	$http.get('/api/states/').then(function(data){
	    $scope.states = data.data;
	});
    }

    loadStates();    
    
	
    
    $log.log("Hello from main controller");
}]);
    
