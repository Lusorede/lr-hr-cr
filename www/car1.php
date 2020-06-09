<?php
//create a rainbow for 10 leds on channel 1:  
send_to_leds_fill_red("fill 1,FF0000,0,40");  
function send_to_leds_fill_red ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
sleep(1);
echo "Car with 1 tabs"; 
?>
