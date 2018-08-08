<?php
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];

if (!empty($first_name) || !empty($first_name) )
	{
 $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "webdb";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {
     $INSERT = "INSERT Into Customer (first_name, last_name) values(?, ?)";
     //Prepare statement
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("s", $first_name);
     $stmt->execute();
     $stmt->bind_result($first_name);
     $stmt->store_result();
     $rnum = $stmt->num_rows;
     if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("ssssii", $first_name , $last_name);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "Problem";
     }
     $stmt->close();
     $conn->close();
    }
} else {
 echo "All field are required";
 die();
}
?>