angular.module('myApp', []).controller('invCtrl', function($scope,$http) {
$scope.tradeId = '';
$scope.price = '';
$scope.num = '';
$scope.investor = '';
$scope.stockName = '';

$scope.invs = [
{tradeId:1, price:11, num:10,investor:'tom',stockName:'APPL'},
{tradeId:2, price:12, num:10,investor:'tom',stockName:'APPL'},
{tradeId:3, price:13, num:10,investor:'tom',stockName:'APPL'},
{tradeId:4, price:14, num:10,investor:'tom',stockName:'APPL'},
{tradeId:5, price:15, num:10,investor:'tom',stockName:'APPL'},
{tradeId:6, price:16, num:10,investor:'tom',stockName:'APPL'},
];

$http({
	headers: {'Content-Type': 'application/json; charset=utf-8'},

    method: 'GET',
    url: 'http://127.0.0.1:8000/investment/all/'
}).then(function successCallback(response) {

        $scope.invs=response.data.investment
    }, function errorCallback(response) {
		alert("get data failed")
});



$scope.incomplete = true; 

$scope.delInv = function(id) {
	
	$http({
	headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
	transformRequest: function(obj) {
                   var str = [];
                   for (var p in obj) {
                       str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                   }
                   return str.join("&");
               },
	xhrFields: { withCredentials: true },
    method: 'POST',
	data:{tradeId:id,dsa:"ads"},
    url: 'http://127.0.0.1:8000/investment/del/'
}).then(function successCallback(response) {
		
		$http({
			headers: {'Content-Type': 'application/json; charset=utf-8'},

			method: 'GET',
			url: 'http://127.0.0.1:8000/investment/all/'
		}).then(function successCallback(response) {

        $scope.invs=response.data.investment
		}, function errorCallback(response) {
			alert("get data failed")
	});
		
		
		
		alert("delete success")
    }, function errorCallback(response) {
		alert("del failed")
});

};

$scope.addInv = function(id) {
    if(!$scope.incomplete){
		$scope.invs.push(
		{
			tradeId:$scope.tradeId,
			price:$scope.price,
			num:$scope.num,
			investor:$scope.investor,
			stockName:$scope.stockName,
		}
		)
		alert("successful saved")
	}
	
//***********************************************	
	
		$http({
	headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
	transformRequest: function(obj) {
                   var str = [];
                   for (var p in obj) {
                       str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                   }
                   return str.join("&");
               },
	xhrFields: { withCredentials: true },
    method: 'POST',
	data:{
			price:$scope.price,
			num:$scope.num,
			investor:$scope.investor,
			stockName:$scope.stockName,
		},
		
    url: 'http://127.0.0.1:8000/investment/add/'
}).then(function successCallback(response) {
		
		$http({
			headers: {'Content-Type': 'application/json; charset=utf-8'},

			method: 'GET',
			url: 'http://127.0.0.1:8000/investment/all/'
		}).then(function successCallback(response) {

        $scope.invs=response.data.investment
		}, function errorCallback(response) {
			alert("get data failed")
		});
		
		
		
		alert("add success")
    }, function errorCallback(response) {
		alert(response)
		alert("add failed")
});
		
//***********************************************	
	
	$scope.incomplete = true;
	$scope.tradeId = '';
	$scope.price = '';
	$scope.num = '';
};


$scope.$watch('tradeId',function() {$scope.test();});
$scope.$watch('price',function() {$scope.test();});
$scope.$watch('num', function() {$scope.test();});
$scope.$watch('investor', function() {$scope.test();});
$scope.$watch('stockName', function() {$scope.test();});

$scope.test = function() {

  $scope.incomplete = false;
  if (!$scope.tradeId.length ||
  !$scope.price.length ||
  !$scope.num.length || !$scope.investor.length || !$scope.stockName.length) {
     $scope.incomplete = true;
  }
};

});