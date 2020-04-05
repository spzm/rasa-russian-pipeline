from rasa.nlu.featurizers.featurizer import DenseFeaturizer

import tensorflow_hub as hub
import tensorflow as tf

class UniversalSentenceEncoderFeaturizer(DenseFeaturizer):
    """Appends a universal sentence encoding to the message's text_features."""

    # URL of the TensorFlow Hub Module
    # TFHUB_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"
    # Load ELMo model from deeppavlov.ai
    # http://docs.deeppavlov.ai/en/master/features/pretrained_vectors.html#elmo
    # TFHUB_URL = "http://files.deeppavlov.ai/deeppavlov_data/elmo_ru-news_wmt11-16_1.5M_steps.tar.gz"
    TFHUB_URL = "https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/embedder/elmo_ru_wiki.json"

    name = "custom_featurizer"

    def required_components(self):
        return []

    def __init__(self, component_config):
        super(UniversalSentenceEncoderFeaturizer, self).__init__(component_config)

        # Load the TensorFlow Hub Module with pre-trained weights
        # Models can differ based on Tensorflow version
        model = hub.load(self.TFHUB_URL)
        if model.signatures.get('default') is not None:
            print('RUNNING V1')
            self.model = model.signatures['default']
            self.version = 'v1'
        else:
            print('RUNNING V2')
            self.model = model
            self.version = 'v2'

    def embed(self, message):
        return self.model(message)

    def train(self, training_data, config, **kwargs):
        # Nothing to train, just process all training examples so that the
        # feature is set for future pipeline steps
        for example in training_data.training_examples:
            self.process(example)

    def process(self, message, **kwargs):
        # Get the sentence encoding by feeding the message text and computing
        # the encoding tensor.
        sentence = tf.constant([message.text])
        feature_vector = self.embed(sentence)
        if self.version == 'v2':
            feature_vector = feature_vector[0]
        # Concatenate the feature vector with any existing text features
        features = self._combine_with_existing_dense_features(message, feature_vector)
        # Set the feature, overwriting any existing `text_features`
        message.set("text_features", features)
