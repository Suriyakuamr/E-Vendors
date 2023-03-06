<?php
$n=$_POST['pno'];
$con=mysqli_connect("localhost","root","","test");
$sql="INSERT INTO login(pno) values('$n')";
$r=$mysqli_query($con,$sql);
if($r)
{
echo "sucess";
}
else
{
echo "failed";
}

?>