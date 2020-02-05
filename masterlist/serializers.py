from rest_framework import serializers

from .models import VehicleMasterList


class vehicleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VehicleMasterList
        fields = (
            'id' ,'Activity_Id' ,'NO' ,'PLATE_NO' ,'CS_NO' ,'CR_NAME' ,'PLATE_ENDING' ,'REGISTRATION_MONTH' ,'MODEL' ,
            'BRAND' ,'VEHICLE_MAKE' ,'ENGINE_NO' ,'CHASSIS_NO' ,'MV_FILE_NO' ,'VEHICLE_TYPE' ,'ASSIGNEE_LAST_NAME' ,
            'ASSIGNEE_FIRST_NAME' ,'VEHICLE_CATEGORY' ,'BAND_LEVEL'  ,'BENEFIT_GROUP' ,'COST_CENTER' ,'GROUP' ,
            'DIVISION' ,'DEPARTMENT' ,'SECTION' ,'IS_ID' ,'IS_LAST_NAME' ,'IS_FIRST_NAME' ,'LOCATION' ,'ORIGINAL_OR_DATE' ,
            'ACQ_DATE' ,'ACQ_COST' ,'ASSET_NO' ,'EQUIPMENT_NO' ,'PO_NO' ,'PLATE_NUMBER_RELEASE_DATE' ,'Employee'
        )
        # Specifying fields in datatables_always_serialize
        # will also force them to always be serialized.
        datatables_always_serialize = ('id','Activity_Id')


# class AlbumSerializer(serializers.ModelSerializer):
#     artist_name = serializers.ReadOnlyField(source='artist.name')
#     # DRF-Datatables can deal with nested serializers as well.
#     artist = ArtistSerializer()
#     genres = serializers.SerializerMethodField()

#     def get_genres(self, album):
#         return ', '.join([str(genre) for genre in album.genres.all()])

#     # If you want, you can add special fields understood by Datatables,
#     # the fields starting with DT_Row will always be serialized.
#     # See: https://datatables.net/manual/server-side#Returned-data
#     DT_RowId = serializers.SerializerMethodField()
#     DT_RowAttr = serializers.SerializerMethodField()

#     def get_DT_RowId(self, album):
#         return 'row_%d' % album.pk

#     def get_DT_RowAttr(self, album):
#         return {'data-pk': album.pk}

#     class Meta:
#         model = Album
#         fields = (
#             'DT_RowId', 'DT_RowAttr', 'rank', 'name',
#             'year', 'artist_name', 'genres', 'artist',
#         )


