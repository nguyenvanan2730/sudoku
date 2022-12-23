import boto3

def upload_file(file_name):
    # Upload image to S3
    path='/Users/nguyenvanan2730/Projects/Sudoku-AWS/sudoku/Images/crop-input-image/'
    local_file_url=path+file_name+'.png'
    s3 = boto3.resource('s3')

    #Count the number of object in 'dev-sudoku-user-input-image' budget
    my_bucket = s3.Bucket('dev-sudoku-user-input-image')
    count_obj=int(0)
    for my_bucket_object in my_bucket.objects.all():
        count_obj+=1   
    print ("Numbers of the object is: ",count_obj)

    #File name of the image in budget
    obj_name='user-input-image-'+str(count_obj+1)+'.png'
    try:
        s3.meta.client.upload_file(local_file_url, 'dev-sudoku-user-input-image', obj_name)
        print("Successfully upload the image to S3:",file_name)
        return obj_name
    except:
        print("Can not upload the image to S3")
        return 0