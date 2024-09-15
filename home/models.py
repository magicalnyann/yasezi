from django.db import models

class BannerImage(models.Model):
    image = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.alt_text or "Banner Image"

class ReviewImage(models.Model):
    image = models.ImageField(upload_to='reviews/')
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.alt_text or "Review Image"


class ReviewImage2(models.Model):
    image = models.ImageField(upload_to='reviews2/')
    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.alt_text or "Review Image"



class SpecialOffer(models.Model):
    image = models.ImageField(upload_to='special_offers/')
    description = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.description or "Special Offer"


from django.db import models

class CompanyInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)  # 이미지 필드 추가

    def __str__(self):
        return self.title

class CompanyVideo(models.Model):
    company_info = models.ForeignKey(CompanyInfo, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='company_videos/')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description or "Company Video"
