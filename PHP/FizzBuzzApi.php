<?php

/** FizzBuzz REST api allowing GET requests in the following format: domain.com/api/fizzbuzz/100
 *  where 100 could be any number
 *  To use this api just require the class and call:
 *  $api = new Api();
 *  echo $api->run();
 *  Author: @absolutic
 */
class FizzBuzzApi
{
    /**
     * @var string
     */
    public $apiName = 'api';

    /**
     * @var array
     */
    public $actions = [
        'fizzbuzz' => 'fizzBuzzAction'
    ];

    /**
     * @var string
     */
    protected $method = 'GET';

    /**
     * @var array
     */
    public $requestUri = [];

    /**
     * Api constructor.
     */
    public function __construct()
    {
        // Set headers to allow client requests
        header("Access-Control-Allow-Orgin: *");
        header("Access-Control-Allow-Methods: GET");
        header("Content-Type: application/json");

        // Read Url and params to properties
        $this->requestUri = explode('/', trim($_SERVER['REQUEST_URI'],'/'));

        // If request method is not GET return error
        if ($this->method !== $_SERVER['REQUEST_METHOD']) {
            return $this->response('Invalid request method');
        }
    }

    /**
     * @return mixed
     */
    public function run()
    {
        if (array_shift($this->requestUri) !== $this->apiName) {
            throw new RuntimeException('API not found', 404);
        }

        $uriAction = array_shift($this->requestUri);
        if (!in_array($uriAction, array_keys($this->actions))) {
            throw new RuntimeException('Action not found', 404);
        } else {
            $action = $this->actions[$uriAction];
        }

        // Check and run api method
        if (method_exists($this, $action)) {
            return $this->{$action}();
        } else {
            throw new RuntimeException('Invalid Method', 405);
        }
    }

    /**
     *
     */
    public function fizzBuzzAction()
    {
        $number = array_shift($this->requestUri);
        $result = [];
        foreach (range(1, $number) as $i) {
            $result[] = $this->fizzbuzz($i, 15, 'FizzBuzz')
                ?: $this->fizzbuzz($i, 5, 'Fizz')
                    ?: $this->fizzbuzz($i, 3, 'Buzz') ?: $i;
        }
        return $this->response($result, 200);
    }

    /**
     * @param $val
     * @param $num
     * @param $str
     * @return bool
     */
    protected function fizzBuzz($val, $num, $str)
    {
        return $val % $num == 0 ? $str : false;
    }

    /**
     * @param $data
     * @param int $status
     * @return false|string
     */
    protected function response($data, $status = 500)
    {
        header("HTTP/1.1 " . $status . " " . $this->requestStatus($status));
        return json_encode($data);
    }

    /**
     * @param $code
     * @return mixed
     */
    private function requestStatus($code)
    {
        $status = array(
            200 => 'OK',
            404 => 'Not Found',
            405 => 'Method Not Allowed',
            500 => 'Internal Server Error',
        );
        return $status[$code]?: $status[500];
    }
}
