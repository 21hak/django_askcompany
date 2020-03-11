from django.db import models

# Create your models here.


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')  # 고품질 이미지 : imagemagic과 같은 라이브러리 사용  
    # upload_to에는 함수도 지정 가능.
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custom object{self.id}"
