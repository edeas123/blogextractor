from blogextractor.extractors.comment import NairalandCommentExtractor
from blogextractor.extractors.forum import NairalandForumExtractor


# leave this here temporarily
# use a factory function to return the appropriate extractor class
def get_extractor(blog: str, type: str):

    return {
        'nairaland':
            {
                'forum': NairalandForumExtractor,
                'comment': NairalandCommentExtractor
            }
    }[blog][type]
