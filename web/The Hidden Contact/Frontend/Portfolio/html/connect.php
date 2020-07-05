<?php
    $fname = $_POST['fname'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    //Database connection
    $conn = new mysqli('http://localhost:8081','root','myadmin123','Contact');
    if($conn->connect_error){
        die('Connection Failed :'.$conn->connect_error);

    }else{
        $stmt = $conn->prepare("insert into registration(fname,email,message)
            values(?,?,?)")
            $stmt->bind_param("sss",$fname , $email , $message);
            $stmt->excute();
            echo "Message sent by $fname";
            $stmt->close();
            $conn->close();
    }
?>