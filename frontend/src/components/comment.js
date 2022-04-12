/**
 * A modern blog web app
 *
 * Created by Nguyen Truong Thinh
 * Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
 */

import axios from "axios";
import Tribute from "tributejs";
import camelcaseKeys from "camelcase-keys";
import snakecaseKeys from "snakecase-keys";

async function getEmojisTribute(commentsForm) {
  const url = "https://api.github.com/emojis";
  let tribute;

  try {
    const response = await axios.get(url);
    const data = camelcaseKeys(response.data, {deep: true});

    let values = [];

    for(const key in data) {
      const value = data[key];
      values.push({
        key: key,
        value: value,
      });
    }

    tribute = new Tribute({
      trigger: ':',
      values: values,
      menuItemTemplate: function(item) {
        return `<img src="${item.original.value}"/>&nbsp;<small>:${item.original.key}:</small>`;
      },
      selectTemplate: function(item) {
        return `:${item.original.key}:`;
      }, 
      menuItemLimit: 5,
    });

  } catch (e) {
    console.error(e);
  }

  return tribute;
}

async function getMentionTribute(commentsForm) {
  const url = commentsForm.dataset.mentionUrl;
  let tribute;

  try {
    const params = {
      objectPk: commentsForm.dataset.objectPk,
      contentType: commentsForm.dataset.contentType,
    };

    const response = await axios.get(url, {
      params: snakecaseKeys(params, { deep: true }),
    });

    const data = camelcaseKeys(response.data, { deep: true });

    let values = [];

    for (const index in data.result) {
      const userValue = data.result[index];
      values.push({
        key: userValue.userName,
        value: userValue.userName,
      });
    }

    tribute = new Tribute({
      values: values,
    });
  } catch (e) {
    console.error(e);
  }

  return tribute;
}

function setupComment() {
  document.addEventListener("DOMContentLoaded", function () {
    const commentsForm = document.getElementsByClassName("comments-form")[0];
    const editorTextArea = document.getElementById("id_comment");

    getMentionTribute(commentsForm).then(function (tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });

    getEmojisTribute(commentsForm).then(function(tribute) {
      if (tribute) {
        tribute.attach(editorTextArea);
      }
    });
  });
}

export { setupComment };
