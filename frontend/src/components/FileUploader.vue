<template>
    <input type="file" accept="image/png, image/jpeg" @change="changeFile"/>
    <button :disabled="file === undefined" @click="upload">Prześlij</button>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-facing-decorator';
import axios from 'redaxios';

@Component
export default class FileUploader extends Vue {
    file: File | undefined

    async changeFile(event: Event){
        let input = event.target as HTMLInputElement;

        if (!input.files?.length){
            return;
        }       

        this.file = input.files[0];
    }

    async upload(){     
        var formData = new FormData();
        formData.append('image', this.file!);

        axios.post('api/classify', formData)
        .then(res => console.log(res.data['class']))
        .catch(_ => console.log('Problem z serwerem.'));
    }
}

</script>