<?php
$file = $_FILES['file'];
$ext = pathinfo($file['name'])['extension'];
$fileName = time() . '.' . $ext;
if (move_uploaded_file($file['tmp_name'], './uploads/' . $fileName)) {
    echo json_encode([
        'code' => 1,
        'msg' => '上传成功',
        'file_url' => '/demo/uploads/' . $fileName
    ]);
}else{
    echo json_encode([
        'code' => 0,
        'msg' => '上传失败',
    ]);
}