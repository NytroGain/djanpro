﻿
<?php 
session_start ();
if (isset($_SESSION['post'])){
    $post=$_SESSION['post'];
}else{
    $post=array();
}
if (isset($_SESSION['error'])){
    $error=$_SESSION['error'];
}else{
    $error=array();
}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>กรอกข้อมูลสำหรับการติดต่อ</title>
<style type="text/css">
.style1 {color: #FF0000}
.style10 {color: #FF6666}
.style11 {font-size: 24px}
.style12 {color: #FF6666; font-weight: bold; }
</style>
</head>

<body>
<form id="form1" name="form1" method="post" action="insert.php">
  <p><strong><span class="style10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="style11">กรอกข้อมูลสำหรับการติดต่อ</span></span></strong></p>
  <table width="100%" border="1" align="center" bgcolor="#FFCCCC">
    <tr>
      <td width="24%">
        <div align="right">
      ชื่อร้าน/สวน :</div></td>
      <td width="76%"><input type="text" name="nameth" id="nameth" value="<?php echo isset($post['nameth']) ? $post['nameth'] : '';?>" /></td>
    </tr>
    <tr>
      <td><div align="right">ชื่อร้าน/สวน (ภาษาอังกฤษ) :</div></td>
      <td><input type="text" name="nameeg" id="nameeg" value="<?php echo isset ($post['nameeg'])? $post['nameeg'] : '';?>"/>
        <span class="style1">*<?php echo isset ($error['nameeg'])? $error['nameeg'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">รายละเอียดเกี่ยวกับร้านหรือสวน :</div></td>
      <td><textarea name="detail" id="detail" cols="45" rows="5"><?php echo isset ($post['detail'])? $post['detail'] : '';?></textarea> 
        <span class="style1">*<?php echo isset ($error['detail'])? $error['detail'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">ที่อยู่ :</div></td>
      <td><textarea name="address" id="address" cols="45" rows="5"><?php echo isset ($post['address'])? $post['address'] : '';?></textarea>
        <span class="style1">*<?php echo isset ($error['address'])? $error['address'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">จังหวัด :</div></td>
      <td><label>
        <input type="text" name="province" id="province" value="<?php echo isset ($post['province'])? $post['province'] : '';?>"/>
        <span class="style1">*<?php echo isset ($error['province'])? $error['province'] : '';?></span></label></td>
    </tr>
    <tr>
      <td><div align="right">โทรศัพท์ :</div></td>
      <td><input type="text" name="tel1" id="tel1" value="<?php echo isset ($post['tel1'])? $post['tel1'] : '';?>" /> 
        <span class="style1">*<?php echo isset ($error['tel1'])? $error['tel1'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">Fax :</div></td>
      <td><input type="text" name="fax" id="fax" value="<?php echo isset ($post['fax'])? $post['fax'] : '';?>" /></td>
    </tr>
    <tr>
      <td><div align="right">Website http://</div></td>
      <td><input type="text" name="webs" id="webs" value="<?php echo isset ($post['webs'])? $post['webs'] : '';?>" />Ex. www.yourweb.com </td>
    </tr>
    <tr>
      <td class="style12">ข้อมูลติดต่อ</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><div align="right">ชื่อ-สกุล :</div></td>
      <td><input type="text" name="name" id="name" value="<?php echo isset ($post['name'])? $post['name'] : '';?>" />
        <span class="style1">*<?php echo isset ($error['name'])? $error['name'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">เพศ :</div></td>
      <td><input name="gender" type="radio" id="radio" value="ชาย" checked="checked" <?php isset($post['gender'])? "checked" :'';
       ?> />
        ชาย 
        <input type="radio" name="gender" id="radio2" value="หญิง" <?php isset($post['gender'])? "checked" :'';
       ?> />
        หญิง</td>
    </tr>
    <tr>
      <td><div align="right">E-mail :</div></td>
      <td><input type="text" name="email" id="email" value="<?php echo isset ($post['email'])? $post['email'] : '';?>" /></td>
    </tr>
    <tr>
      <td><div align="right">เบอร์โทรศัพท์ (เบอร์ภายใน) :</div></td>
      <td><input type="text" name="tel2" id="tel2" value="<?php echo isset ($post['tel2'])? $post['tel2'] : '';?>" />
        <span class="style1">*<?php echo isset ($error['tel2'])? $error['tel2'] : '';?></span></td>
    </tr>
    <tr>
      <td><div align="right">เบอร์มือถือ :</div></td>
      <td><input type="text" name="mobile" id="mobile" value="<?php echo isset ($post['mobile'])? $post['mobile'] : '';?>" /></td>
    </tr>
    <tr>
      <td colspan="2"><div align="center">
        <input type="submit" name="button" id="button" value="ตกลง" />
        <input type="reset" name="button2" id="button2" value="ยกเลิก" />
      </div></td>
    </tr>
  </table>
</form>
</body>
</html>