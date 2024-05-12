# posts > serializers.py
# 주의! DRF는 TextField를 지원하지 않음. -> CharField로 내부적으로 긴 문자열을 받을 수 있음.

from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField()
    writer = serializers.IntegerField()
    bad_post = serializers.BooleanField()


        # create 추가
    def create(self, validated_data):
        writer_id = validated_data['writer']  # validated_data에서 writer 필드로부터 사용자의 ID를 가져옴
        writer_instance = User.objects.get(id=writer_id)  # 해당 ID를 가진 사용자의 인스턴스를 가져옴

        post = Post.objects.create(
            content=validated_data['content'],
            view_count=validated_data['view_count'],
            writer=writer_instance,  # 가져온 사용자의 인스턴스를 writer 필드에 할당
        )
        return post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# class CommentSerializer(serializers.Serializer):
#     image = serializers.ImageField(required=False)
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(required=False)
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#     writer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # posts > serializers.py

# # ModelSerializer
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
        # return Post.objects.create(validated_data)
    # def create(self, validated_data):
    #     writer_id = validated_data.pop('writer_id', None)  # writer_id 필드에서 사용자의 ID 값을 가져옴
    #     print(writer_id)
    #     writer_instance = None
    #     if writer_id is not None:
    #         writer_instance = User.objects.get(id=writer_id)  # 해당 ID를 가진 사용자 객체를 가져옴

    #     post = Post.objects.create(
    #         content=validated_data['content'],
    #         view_count=validated_data['view_count'],
    #         writer=writer_instance,  # 가져온 사용자 객체를 writer 필드에 할당
    #     )
    #     return post



