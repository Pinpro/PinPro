<template>
  <div class="pin-preview-modal">
    <section>
        <div class="card">
          <div class="card-image">
            <figure class="image">
              <img :src="pinItem.large_image_url" alt="Image">
            </figure>
          </div>
          <div class="card-content">
            <div class="content">
                <p class="description title">{{ pinItem.description }}</p>
            </div>
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img :src="pinItem.avatar" alt="Image">
                </figure>
              </div>
              <div class="media-content">
                <div class="is-pulled-left">
                  <p class="title is-4 pin-meta-info"><span class="dim">Pinned by </span><span class="author">{{ pinItem.author }}</span></p>
                  <div v-if="hasLiked" class="heart" @click="deleteCollect()"></div>
                  <div v-else class="heartGrey" @click="addCollect()"></div>
                  <p class="subtitle is-6" v-show="pinItem.tags.length > 0">
                    <span class="subtitle dim">in&nbsp;</span>
                    <template v-for="tag in pinItem.tags">
                      <b-tag v-bind:key="tag" type="is-info" class="pin-preview-tag">{{ tag }}</b-tag>
                    </template>
                  </p>
                </div>
                <div class="is-pulled-right">
                  <a :href="pinItem.referer" target="_blank">
                    <b-button
                        v-show="pinItem.referer !== null"
                        class="meta-link"
                        type="is-warning">
                      Referer
                    </b-button>
                  </a>
                  <a :href="pinItem.original_image_url" target="_blank">
                    <b-button
                        v-show="pinItem.original_image_url !== null"
                        class="meta-link"
                        type="is-link">
                        Original Image
                    </b-button>
                  </a>
                  <b-button
                      @click="closeAndGoTo"
                      class="meta-link"
                      type="is-success">
                      Goto Pin Link
                  </b-button>
                </div>
              </div>
            </div>
          </div>
        </div>
    </section>
  </div>
</template>

<script>
import API from './api';
import modals from './modals';

function initialData() {
  return {
    hasLiked: false,
    userLoggedIn: false,
  };
}

export default {
  name: 'PinPreview',
  data() {
    return initialData();
  },
  props: ['pinItem', 'loggedIn'],
  methods: {
    closeAndGoTo() {
      this.$parent.close();
      this.$router.push(
        { name: 'pin', params: { pinId: this.pinItem.id } },
      );
    },
    addCollect() { // 点赞
      if (!this.loggedIn) {
        modals.openLogin(this, this.onLoginSucceed);
      }
      API.addLike({
        pin: this.pinItem.id,
      }).then((response) => {
        console.log(response.data);
        this.hasLiked = true;
      }).catch((error) => {
        console.log(error);
      });
    },
    deleteCollect() {
    // 取消点赞
      API.delLike(this.pinItem.id).then((response) => {
        console.log(response.data);
        console.log(this.pinItem.id);
        this.hasLiked = false;
      }).catch((error) => {
        console.log(error);
      });
    },
    checkLikeFlg() {
      API.checkIfLike(this.pinItem.id).then((response) => {
        console.log(response.data);
        this.hasLiked = true;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  created() {
    if (this.loggedIn) {
      this.checkLikeFlg();
    }
  },
};
</script>

<style lang="scss" scoped>
@import './utils/fonts.scss';

.meta-link {
  margin-left: 0.3rem;
}
.dim {
  @include secondary-font-color-in-dark;
}
.pin-meta-info {
  line-height: 16px;
}
.card {
  background-color: rgba(0, 0, 0, 0.6);
  .content {
    border-bottom: 1px solid #333;
  }
  .card-content {
    .author {
      @include title-font-color-in-dark;
    }
    padding: 0;
    .content {
      padding: 0.3rem;
      margin-bottom: 0;
    }
    .media {
      padding: 0.3rem;
    }
  }
  .description {
    @include title-font;
    @include title-font-color-in-dark;
    font-size: 16px;
    padding: 8px;
  }
}
.pin-preview-tag {
  margin-right: 0.2rem;
  margin-bottom: 2px;
}
/* preview size should always less then screen */
.card-image img {
  width: 100%;
}

.heart{
    position: relative;
    width: 100px;
    height: 90px;
    float: left;
}
.heart:before,
.heart:after{
    position: absolute;
    content: "";
    left: 50px;
    top: 0;
    width: 50px;
    height: 80px;
    background: #fc2e5a;
    -moz-border-radius: 50px 50px 0 0;
    border-radius: 50px 50px 0 0;
    -webkit-transform: rotate(-45deg);
       -moz-transform: rotate(-45deg);
        -ms-transform: rotate(-45deg);
         -o-transform: rotate(-45deg);
            transform: rotate(-45deg);
    -webkit-transform-origin: 0 100%;
       -moz-transform-origin: 0 100%;
        -ms-transform-origin: 0 100%;
         -o-transform-origin: 0 100%;
            transform-origin: 0 100%;
}
.heart:after{
    left: 0;
    -webkit-transform: rotate(45deg);
       -moz-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
         -o-transform: rotate(45deg);
            transform: rotate(45deg);
    -webkit-transform-origin: 100% 100%;
       -moz-transform-origin: 100% 100%;
        -ms-transform-origin: 100% 100%;
         -o-transform-origin: 100% 100%;
            transform-origin :100% 100%;
}
.heartGrey{
    position: relative;
    width: 100px;
    height: 90px;
    float: left;
}
.heartGrey:before,
.heartGrey:after{
    position: absolute;
    content: "";
    left: 50px;
    top: 0;
    width: 50px;
    height: 80px;
    background: #e2e1e1;
    -moz-border-radius: 50px 50px 0 0;
    border-radius: 50px 50px 0 0;
    -webkit-transform: rotate(-45deg);
       -moz-transform: rotate(-45deg);
        -ms-transform: rotate(-45deg);
         -o-transform: rotate(-45deg);
            transform: rotate(-45deg);
    -webkit-transform-origin: 0 100%;
       -moz-transform-origin: 0 100%;
        -ms-transform-origin: 0 100%;
         -o-transform-origin: 0 100%;
            transform-origin: 0 100%;
}
.heartGrey:after{
    left: 0;
    -webkit-transform: rotate(45deg);
       -moz-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
         -o-transform: rotate(45deg);
            transform: rotate(45deg);
    -webkit-transform-origin: 100% 100%;
       -moz-transform-origin: 100% 100%;
        -ms-transform-origin: 100% 100%;
         -o-transform-origin: 100% 100%;
            transform-origin :100% 100%;
}
</style>
