<?php
//
// A very simple PHP example that sends a HTTP POST to a remote site
//

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL,"http://www.socialsecurity.gov/OACT/babynames/#ht=1");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS,
            "year=1990&top=1000&number=n&submit=%20%20Go%20%20");

$result = curl_exec ($ch);
curl_close ($ch);
?>