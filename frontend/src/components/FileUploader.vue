<template>
    <div class="image-preview-container" v-if="fileUrl !== null">
        <img class="image-preview" :src="fileUrl" draggable="false"/>
    </div>
    <input type="file" accept="image/jpg, image/jpeg" @change="changeFile"/>
    <button :disabled="file === undefined" @click="upload">Prześlij</button>
</template>

<script lang="ts">
import { Component, Emit, Vue } from 'vue-facing-decorator';
import axios from 'redaxios';

@Component
export default class FileUploader extends Vue {
    file: File | undefined
    fileUrl: string | null = null

    @Emit('change-classification')
    changeClassification(cls: string | null): string | null {
        return cls;
    }

    async changeFile(event: Event){
        let input = event.target as HTMLInputElement;
        this.changeClassification(null);

        if (!input.files?.length){
            this.file = undefined
            this.fileUrl = null
            return;
        }       

        this.file = input.files[0];
        this.fileUrl = URL.createObjectURL(this.file);
    }

    async upload(){     
        var formData = new FormData();
        formData.append('image', this.file!);

        axios.post('api/classify', formData)
        .then(res => 
        {
            let cls = res.data['class'];
            this.changeClassification(cls);
            console.log(cls);
        })
        .catch(err => {
            this.changeClassification(null);
            console.log('Problem z serwerem.');
            console.log(err)
        });
    }
}

</script>

<style>
.image-preview-container{
    width: 400px;
    height: 400px;
    margin: 20px;
}

.image-preview{
    width: 100%;
    height: 100%;
    object-fit: contain;
}

</style>