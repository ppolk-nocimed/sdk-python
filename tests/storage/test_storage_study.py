import logging
from pathlib import Path

import pytest
from dynaconf import settings

from ambra_sdk.exceptions.storage import (
    AmbraResponseException,
    NotFound,
    PermissionDenied,
    UnsupportedMediaType,
)
from ambra_sdk.service.ws import WSManager

logger = logging.getLogger(__name__)


class TestStorageStudy:
    """Test Study namespace of Storage api."""

    @pytest.fixture(scope='class')
    def image(self, api, readonly_study):
        """First study image."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        schema = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        return schema.series[0]['images'][0]

    @pytest.fixture(scope='class')
    def logo_attachment(self, api, readonly_study):
        """Ambra logo attachment."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid
        logo = Path(__file__) \
            .parents[1] \
            .joinpath('images', 'logo.png')
        with open(logo, 'rb') as f:
            api.Storage.Study.post_attachment(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
                opened_file=f,
            )
        schema = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        attachment = schema.attachments[0]
        yield attachment
        api.Storage.Study.delete_attachment(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            attachment_id=attachment['id'],
            hash_arg=attachment['version'],
        )

    def test_all_methods_prepared(self, api):
        """Test all methods have only prepare argument."""
        study = api.Storage.Study
        for attribute_name in dir(study):  # NOQA:WPS421
            if not attribute_name.startswith('_'):
                attribute = getattr(study, attribute_name)
                if callable(attribute):
                    assert 'only_prepare' in \
                        attribute.__func__.__code__.co_varnames  # NOQA:WPS609

    def test_schema_prepared(self, api, readonly_study):
        """Test schema prepared method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        prepared = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            only_prepare=True,
        )
        assert prepared.url

    def test_schema(self, api, readonly_study):
        """Test schema method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        schema = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert schema

    def test_delete(self, api, account, auto_remove):
        """Test delete method."""
        study_dir = Path(__file__) \
            .parents[1] \
            .joinpath('dicoms', 'anonymize')
        study = api.Addon.Study.upload_and_get(
            study_dir=study_dir,
            namespace_id=account.account.namespace_id,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('Uploaded study %s', study.uuid)
        auto_remove(study)

        engine_fqdn = study.engine_fqdn
        storage_namespace = study.storage_namespace
        study_uid = study.study_uid

        delete = api.Storage.Study.delete(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert delete.status_code in {200, 202}

    def test_delete_image(
        self,
        api,
        account,
        auto_remove,
        storage_auto_remove,
    ):
        """Test delete_image method."""
        study_dir = Path(__file__) \
            .parents[1] \
            .joinpath('dicoms', 'anonymize')
        study = api.Addon.Study.upload_and_get(
            study_dir=study_dir,
            namespace_id=account.account.namespace_id,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('Uploaded study %s', study.uuid)
        auto_remove(study)

        engine_fqdn = study.engine_fqdn
        storage_namespace = study.storage_namespace
        study_uid = study.study_uid
        storage_auto_remove(
            engine_fqdn,
            storage_namespace,
            study_uid,
        )

        schema = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        image = schema.series[0]['images'][0]

        delete_image = api.Storage.Study.delete_image(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
        )
        assert delete_image.status_code in {200, 202}

        with pytest.raises(NotFound):
            delete_image = api.Storage.Study.delete_image(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
                image_uid=image['id'],
            )

    def test_count(self, api, readonly_study, image):
        """Test count method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        count = api.Storage.Study.count(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
        )
        assert count

    def test_tag(self, api, readonly_study):
        """Test tag method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid
        phi_namespace = readonly_study.phi_namespace

        tag = api.Storage.Study.tag(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            phi_namespace=phi_namespace,
        )
        assert tag

    def test_attribute(self, api, readonly_study, image):
        """Test attribute method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        attribute = api.Storage.Study.attribute(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
        )
        assert attribute

    def test_image_phi(self, api, readonly_study, image):
        """Test image_phi method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        image_phi = api.Storage.Study.image_phi(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
        )
        assert image_phi

    def test_phi(self, api, readonly_study):
        """Test phi method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        phi = api.Storage.Study.phi(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert phi

    def test_thumbnail(self, api, readonly_study, image):
        """Test thumbnail method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        thumbnail = api.Storage.Study.thumbnail(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
            frame_number=0,
        )
        assert thumbnail.status_code == 200

    def test_diagnostic(self, api, readonly_study, image):
        """Test diagnostic method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        diagnostic = api.Storage.Study.diagnostic(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
            frame_number=0,
        )
        assert diagnostic.status_code == 200

    def test_frame(self, api, readonly_study, image):
        """Test frame method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        frame = api.Storage.Study.frame(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
            frame_number=0,
        )
        assert frame.status_code == 200

    def test_frame_tiff(self, api, readonly_study, image):
        """Test frame tiff method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        # TODO test with tiff data.
        # Current study have not tiff dicoms.
        with pytest.raises(AmbraResponseException):
            api.Storage.Study.frame_tiff(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
                image_uid=image['id'],
                image_version=image['version'],
                frame_number=0,
            )

    def test_pdf(self, api, readonly_study, image):
        """Test pdf method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        # TODO: Check with pdf dicoms
        with pytest.raises(UnsupportedMediaType):
            api.Storage.Study.pdf(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
                image_uid=image['id'],
                image_version=image['version'],
            )

    def test_image_json(self, api, readonly_study, image):
        """Test image_json method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        image_json = api.Storage.Study.image_json(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            image_uid=image['id'],
            image_version=image['version'],
        )
        assert image_json

        assert len(list(image_json.get_tags(filter_dict={'group': 2}))) == 7
        tag = image_json.tag_by_name('Manufacturer')
        assert tag.group == 8
        assert tag.element == 112
        assert tag.vr == 'LO'
        assert tag.vl == 18
        assert tag.value == 'GE MEDICAL SYSTEMS'

    def test_json(self, api, readonly_study):
        """Test json method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        json = api.Storage.Study.json(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert json
        assert len(list(json[0].get_tags(filter_dict={'group': 2}))) == 7
        tag = json[0].tag_by_name('Manufacturer')
        assert tag.group == 8
        assert tag.element == 112
        assert tag.vr == 'LO'
        assert tag.vl == 18
        assert tag.value == 'GE MEDICAL SYSTEMS'

    def test_post_attachment(self, logo_attachment):
        """Test post_attachment method."""
        # This is tested by logo_attachemnt fixture
        assert logo_attachment

    def test_delete_attachment(self, logo_attachment):
        """Test post_attachment method."""
        # This is tested by logo_attachemnt fixture
        assert logo_attachment

    def test_attachment(
        self,
        api,
        readonly_study,
        logo_attachment,
    ):
        """Test attachment method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        attachment = api.Storage.Study.attachment(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            attachment_id=logo_attachment['id'],
            version=logo_attachment['version'],
        )
        assert attachment.status_code == 200

    def test_latest(self, api, readonly_study, logo_attachment):
        """Test latest method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        latest = api.Storage.Study.latest(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            file_name='latest',
        )
        assert latest.status_code == 200

    def test_download(self, api, readonly_study):
        """Test download method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        download = api.Storage.Study.download(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            bundle='dicom',
        )
        assert download.status_code == 200

    def test_video(self, api, readonly_study, image):
        """Test video method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        # TODO: Check with video dicoms
        with pytest.raises(UnsupportedMediaType):
            api.Storage.Study.video(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
                image_uid=image['id'],
                image_version=image['version'],
            )

    def test_split_one_series(
        self,
        api,
        account,
        readonly_study,
        auto_remove,
    ):
        """Test split method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        split = api.Storage.Study.split(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert split.status_code in {200, 202}
        new_study_uid = split.text
        logger.info('New splitted study %s', new_study_uid)

        new_study = api.Addon.Study.wait(
            study_uid=new_study_uid,
            namespace_id=storage_namespace,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        auto_remove(new_study)
        assert new_study

    def test_split_multi_series(
        self,
        api,
        account,
        multi_series_study,
        auto_remove,
    ):
        """Test split method."""
        engine_fqdn = multi_series_study.engine_fqdn
        storage_namespace = multi_series_study.storage_namespace
        study_uid = multi_series_study.study_uid

        split = api.Storage.Study.split(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
            series_uid='1.2.840.113619.2.278.3.2831165743.908.1345078604.111',
        )

        new_study_uid = split.text
        logger.info('New splitted study %s', new_study_uid)
        assert split.status_code in {200, 202}

        new_study = api.Addon.Study.wait(
            study_uid=new_study_uid,
            namespace_id=storage_namespace,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        auto_remove(new_study)
        assert new_study

    def test_merge(
        self,
        api,
        account,
        auto_remove,
    ):
        """Test merge method.

        Merge is async operation.
        This method append images from one study to another.
        """
        study_dir1 = Path(__file__) \
            .parents[1] \
            .joinpath('dicoms', 'splitted', '1')

        study1 = api.Addon.Study.upload_and_get(
            study_dir=study_dir1,
            namespace_id=account.account.namespace_id,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('Uploaded study %s', study1.uuid)
        auto_remove(study1)

        study_dir2 = Path(__file__) \
            .parents[1] \
            .joinpath('dicoms', 'splitted', '2')

        study2 = api.Addon.Study.upload_and_get(
            study_dir=study_dir2,
            namespace_id=account.account.namespace_id,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('Uploaded study %s', study2.uuid)
        auto_remove(study2)

        engine_fqdn = study1.engine_fqdn
        storage_namespace = study1.storage_namespace

        # Merge is async operation...
        # So we need to wait EDIT event in websocket
        ws_url = '{url}/channel/websocket'.format(url=api._api_url)

        channel_name = 'study.{namespace_id}'.format(
            namespace_id=storage_namespace,
        )
        sid = api.sid
        ws_manager = WSManager(ws_url)

        with ws_manager.channel(sid, channel_name) as ws:
            api.Storage.Study.merge(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study1.study_uid,
                secondary_study_uid=study2.study_uid,
            )
            ws.wait_for_event(
                channel_name,
                sid,
                'EDIT',
                timeout=settings.API['merge_timeout'],
            )

        schema = api.Storage.Study.schema(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study1.study_uid,
        )
        # Actually, merge method merge only images,
        # but in  test fixtures each images have own series.
        # Old study1 have only 2 images.
        assert len(schema.series) == 4

    def test_anonymize(
        self,
        api,
        account,
        readonly_study,
        auto_remove,
        storage_auto_remove,
    ):
        """Test anonymize method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid
        series_uid = '1.2.840.113619.2.278.3.2831165743.908.1345078604.948'

        region = {
            'series': {
                series_uid: {
                    'regions': [
                        {
                            'x': 10,
                            'y': 10,
                            'width': 30,
                            'height': 40,
                        },
                    ],
                },
            },
        }

        anonymize = api.Storage.Study.anonymize(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            to_namespace=storage_namespace,
            study_uid=study_uid,
            region=region,
            color='121197149',
        )
        assert anonymize.status_code in {200, 202}

        new_study_uid = anonymize.text
        storage_auto_remove(
            engine_fqdn,
            storage_namespace,
            new_study_uid,
        )

        # wait for ready new study
        new_study = api.Addon.Study.wait(
            study_uid=new_study_uid,
            namespace_id=storage_namespace,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('New anonymized study %s', new_study.uuid)
        auto_remove(new_study)
        assert new_study

    def test_crop(
        self,
        api,
        account,
        readonly_study,
        auto_remove,
        storage_auto_remove,
    ):
        """Test crop method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid
        series_uid = '1.2.840.113619.2.278.3.2831165743.908.1345078604.948'

        region = {
            'series': {
                series_uid: {
                    'regions': [
                        {
                            'x': 10,
                            'y': 10,
                            'width': 30,
                            'height': 40,
                        },
                    ],
                },
            },
        }

        crop = api.Storage.Study.crop(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            to_namespace=storage_namespace,
            study_uid=study_uid,
            region=region,
        )
        assert crop.status_code in {200, 202}

        new_study_uid = crop.text
        storage_auto_remove(
            engine_fqdn,
            storage_namespace,
            new_study_uid,
        )

        # wait for ready new study
        new_study = api.Addon.Study.wait(
            study_uid=new_study_uid,
            namespace_id=storage_namespace,
            timeout=settings.API['upload_study_timeout'],
            ws_timeout=settings.API['ws_timeout'],
        )
        logger.info('New cropped study %s', new_study.uuid)
        auto_remove(new_study)
        assert new_study

    def test_cache(self, api, readonly_study):
        """Test cache method."""
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid

        cache = api.Storage.Study.cache(
            engine_fqdn=engine_fqdn,
            namespace=storage_namespace,
            study_uid=study_uid,
        )
        assert cache.status_code in {200, 202}

    def test_retry_storage_with_new_sid(self, api, readonly_study):
        """Test retry storage request with new sid.

        In storage PermissionDenied means two things:

        1. Wrong sid
        2. User have not access to some stoudy
        """
        api._sid = 'Wrong sid'
        engine_fqdn = readonly_study.engine_fqdn
        storage_namespace = readonly_study.storage_namespace
        study_uid = readonly_study.study_uid
        try:
            api.Storage.Study.schema(
                engine_fqdn=engine_fqdn,
                namespace=storage_namespace,
                study_uid=study_uid,
            )
        except Exception:
            pytest.fail('Something goes wrong with retrying with new sid')

        # But access denied still works:
        with pytest.raises(PermissionDenied):
            api.Storage.Study.schema(
                engine_fqdn=engine_fqdn,
                namespace='abra',
                study_uid='kadabra',
            )
