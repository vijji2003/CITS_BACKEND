from rest_framework import serializers
from .models import CareerApplication,ContactMessage,MOU,GalleryImage,Project,CommunityItem


class CareerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerApplication
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class MOUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MOU
        fields = "__all__"

class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'category', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class CommunityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityItem
        fields = "__all__"


from .models import CpuInquiry

class CpuInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuInquiry
        fields = '__all__'