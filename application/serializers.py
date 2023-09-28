from rest_framework import serializers


class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_count_view = serializers.IntegerField()
    total_view = serializers.IntegerField()
    total_users_product = serializers.IntegerField()
    percent_products = serializers.FloatField()

    # class Meta:
    #     model =
    #     fields =
